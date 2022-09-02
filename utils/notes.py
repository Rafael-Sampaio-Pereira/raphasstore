react_build_for_django = {
    "build": "rm -rf ../backend/build && react-scripts build && cp -r build ../backend/build && rm -rf build",
}

generic = {
    "obs": "Gunicorn can't serve static files"
}

creation = {
    "react_ts_project": "yarn create react-app projectname --template typescript "
}

"test": "react-scripts test"