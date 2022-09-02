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

 "devDependencies": {
    "@typescript-eslint/eslint-plugin": "5.6.0",
    "@typescript-eslint/parser": "5.6.0",
    "eslint": "^7.32.0",
    "eslint-config-airbnb": "19.0.4",
    "eslint-config-airbnb-base": "15.0.0",
    "eslint-plugin-import": "^2.25.2",
    "eslint-plugin-jsx-a11y": "^6.5.1",
    "eslint-plugin-react": "^7.28.0",
    "eslint-plugin-react-hooks": "^4.3.0",
    "typescript": "^4.4.3"
  }