from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

from .models import Inventory, Product


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField(label="Arquivo com Produtos")


class ProductAdmin(admin.ModelAdmin):
    read_only_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "title",
        "description",
        "price",
        "brand",
        "category",
        "updated_at",
    )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):

        errors = ""
        created_cont = 0
        index_url = reverse("admin:index")

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(
                    request,
                    "Atenção: O arquivo enviado não é válido!"
                )
                return HttpResponseRedirect(request.path_info)

            try:

                # Getting table data
                file_data = csv_file.read().decode("utf8")

                # Split table into lines
                csv_data = file_data.split("\n")

                # for each line in table
                for index, x in enumerate(csv_data):

                    # skip header line
                    if index == 0:
                        continue

                    elif index < len(csv_data):

                        # get line fields, csv must be separetade using ';'
                        fields = x.split(";")
                        print(fields[0])
                        profit = int(fields[7])
                        purchase_price = float(
                            str(fields[6]).replace(",", ".")
                        )

                        _product, created = Product.objects.update_or_create(
                            title=fields[0],
                            brand=fields[1],
                            category=fields[2],
                            description=fields[3],
                            sku=fields[4],
                            # calculate final price using profit_margin +
                            # purchase_price
                            price=round(
                                purchase_price + (
                                    purchase_price * profit / 100
                                ),
                                2
                            ),
                        )

                        if created:
                            Inventory.objects.update_or_create(
                                product=_product,
                                initial_quantity=fields[5],
                                remaning_quantity=fields[5],
                                profit_margin=profit,
                                purchase_price=purchase_price,
                                size=fields[8],
                                color=fields[9],
                            )
                            created_cont += 1

            except Exception as e:
                errors += str(e) + "\n"

            if errors:
                messages.error(
                    request,
                    f"Arquivo .csv processado. {created_cont} "
                    f"produtos cadastrados. Erros {errors}",
                )
            else:
                messages.success(
                    request,
                    f"Arquivo .csv processado. {created_cont} "
                    "produtos cadastrados com sucesso!",
                )
            return HttpResponseRedirect(index_url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class InvetoryAdmin(admin.ModelAdmin):
    read_only_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "product",
        "color",
        "size",
        "initial_quantity",
        "remaning_quantity",
        "purchase_price",
        "profit_margin",
        "created_at",
        "updated_at",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InvetoryAdmin)
