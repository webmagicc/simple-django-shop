var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

var config = require('./webpack.base.config.js')
var localSettings = require('./webpack.local-settings.js')

var ip = localSettings.ip

config.devtool = "#eval-source-map"

config.output.path = require('path').resolve('./simple_django_shop/static/bundles/prod/')

config.ip = ip

// Use webpack dev server
config.entry = {
  
  Main: [
    'webpack-dev-server/client?http://' + ip + ':3000',
    'webpack/hot/only-dev-server',
    './reactjs/Main',
  ]
}

// override django's STATIC_URL for webpack bundles
config.output.publicPath = 'http://' + ip + ':3000' + '/assets/bundles/'

// Add HotModuleReplacementPlugin and BundleTracker plugins
/*
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
  new BundleTracker({filename: './webpack-stats-local.json'}),
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('development'),
      'BASE_API_URL': JSON.stringify('http://' + ip + ':8000/api/v1/'),
  }}),

])
*/

// Add a loader for JSX files with react-hot enabled
config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot', 'babel'] }
)

module.exports = config