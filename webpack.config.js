var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

const NODE_ENV = process.env.NODE_ENV || "development"
module.exports = {
	entry: {
    // Add as many entry points as you have container-react-components here
    Main: './reactjs/Main',
    vendors: ['react'],
  },
  output: {
      path: path.resolve('./simple_django_shop/static/bundles/local/'),
      filename: "[name]-[hash].js"
  },
  watch:NODE_ENV == "development",
  devtool:"source-map",
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({name:'vendors', filename:'vendors.js'}),
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({path: __dirname,filename: './webpack-stats-local.json'})
  ],
  node: {
    fs: "empty"
  },
  resolve: {
    modules: ['node_modules/'],
    extensions: [".webpack.js", ".web.js", '.js', '.jsx', ".json"],
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
}