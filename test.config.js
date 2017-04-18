var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
	entry: {
    Main: './reactjs/Main',
    vendors: ['react'],
  },
  output: {
      path: path.resolve('./simple_django_shop/static/bundles/'),
      filename: "[name].js"
  },
  plugins: [
    new BundleTracker({path: __dirname,filename: './webpack-stats.json'})
  ],
  resolveLoader: {
   moduleExtensions: ["-loader"]
 },
  module: {
    loaders: [{ 
      test: /\.jsx?$/, 
      exclude: /node_modules/,
       loaders: ['babel']

    }] 
  },
  resolve: {
    modules: ['node_modules/'],
    extensions: [".webpack.js", ".web.js", '.js', '.jsx', ".json"],
    alias: {
      'react': path.join(__dirname, 'node_modules', 'react')
    }
  },
}