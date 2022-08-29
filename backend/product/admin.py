from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField(label="Arquivo com Produtos")

class ProductAdmin(admin.ModelAdmin):
    read_only_fields = ('created_at', 'updated_at', )
    list_display = ('title', 'description', 'price', 'brand', 'created_at', 'updated_at',)
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):
        if request.method == 'POST':
            print("Enviando csv para o cadastro de produtos...")
            
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Atenção: O arquivo enviado não é válido!')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode('utf8')
            # Split table into lines
            csv_data = file_data.split('\n')
            
            created_cont = 0
            # for each line in table
            for index, x in enumerate(csv_data):
                # skip header line
                if index == 0:
                    continue
                elif index < len(csv_data)-1:
                    # get line fields, csv must be separetade using ';'
                    fields = x.split(';')
                    profit_margin = int(fields[7])
                    quantity = fields[5], 
                    purchase_price = float(str(fields[6]).replace(',','.'))
                    
                    created = Product.objects.update_or_create(
                        title = fields[0], 
                        brand  = fields[1], 
                        category = fields[2],
                        description = fields[3], 
                        sku = fields[4],
                        purchase_price = purchase_price,
                        # calculate final price using profit_margin + purchase_price
                        price = round(purchase_price + (purchase_price * profit_margin/100), 2))
                    
                    if created:
                        created_cont += 1
            
            url = reverse('admin:index')
            messages.success(
                request, 
                f'Arquivo .csv processado. {created_cont} produtos cadastrados com sucesso!'
            )
            return HttpResponseRedirect(url)   
                
            
        form = CsvImportForm()
        data = {"form": form}
        return render(request, 'admin/csv_upload.html', data)


admin.site.register(Product, ProductAdmin)
