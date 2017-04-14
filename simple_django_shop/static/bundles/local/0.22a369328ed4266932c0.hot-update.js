webpackHotUpdate(0,{

/***/ 1061:
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function(module, process, __dirname) {/* REACT HOT LOADER */ if (true) { (function () { var ReactHotAPI = __webpack_require__(249), RootInstanceProvider = __webpack_require__(250), ReactMount = __webpack_require__(112), React = __webpack_require__(1); module.makeHot = module.hot.data ? module.hot.data.makeHot : ReactHotAPI(function () { return RootInstanceProvider.getRootInstances(ReactMount); }, React); })(); } try { (function () {

'use strict';

var path = __webpack_require__(7);
var webpack = __webpack_require__(248);
var BundleTracker = __webpack_require__(1341);

var NODE_ENV = process.env.NODE_ENV || "development";
module.exports = {
  entry: {
    // Add as many entry points as you have container-react-components here
    Main: './reactjs/Main',
    vendors: ['react']
  },
  output: {
    path: path.resolve('./simple_django_shop/static/bundles/local/'),
    filename: "[name]-[hash].js"
  },
  watch: NODE_ENV == "development",
  devtool: "source-map",
  plugins: [new webpack.optimize.CommonsChunkPlugin({ name: 'vendors', filename: 'vendors.js' }), new webpack.HotModuleReplacementPlugin(), new BundleTracker({ path: __dirname, filename: './webpack-stats-local.json' })],
  node: {
    fs: "empty"
  },
  resolve: {
    extensions: ['.js', '.jsx'],
    alias: {
      'react': path.join(__dirname, 'node_modules', 'react')
    }
  },
  resolveLoader: {
    moduleExtensions: ["-loader"]
  },
  module: {
    loaders: [{
      test: /\.jsx?$/,
      exclude: /node_modules/,
      loaders: ['react-hot', 'babel']
    }]
  }
};

/* REACT HOT LOADER */ }).call(this); } finally { if (true) { (function () { var foundReactClasses = module.hot.data && module.hot.data.foundReactClasses || false; if (module.exports && module.makeHot) { var makeExportsHot = __webpack_require__(251); if (makeExportsHot(module, __webpack_require__(1))) { foundReactClasses = true; } var shouldAcceptModule = true && foundReactClasses; if (shouldAcceptModule) { module.hot.accept(function (err) { if (err) { console.error("Cannot apply hot update to " + "webpack.config.js" + ": " + err.message); } }); } } module.hot.dispose(function (data) { data.makeHot = module.makeHot; data.foundReactClasses = foundReactClasses; }); })(); } }
/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(55)(module), __webpack_require__(0), "/"))

/***/ })

})
//# sourceMappingURL=0.22a369328ed4266932c0.hot-update.js.map