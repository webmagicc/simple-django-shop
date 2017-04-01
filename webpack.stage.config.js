var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

var config = require('./webpack.base.config.js')

config.output.path = require('path').resolve('./djreact/static/bundles/stage/')

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-stage.json'}),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('staging'),
      'BASE_API_URL': JSON.stringify('https://sandbox.example.com/api/v1/'),
  }}),

  // keeps hashes consistent between compilations
  new webpack.optimize.OccurenceOrderPlugin(),

  // minifies your code
  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
])

// Add a loader for JSX files
config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel' }
)

module.exports = config