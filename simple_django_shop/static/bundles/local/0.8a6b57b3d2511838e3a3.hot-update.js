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

/***/ }),

/***/ 1341:
/***/ (function(module, exports, __webpack_require__) {

var path = __webpack_require__(7);
var fs = __webpack_require__(!(function webpackMissingModule() { var e = new Error("Cannot find module \"fs\""); e.code = 'MODULE_NOT_FOUND'; throw e; }()));
var stripAnsi = __webpack_require__(1344);
var mkdirp = __webpack_require__(917);
var extend = __webpack_require__(1342);

var assets = {};
var DEFAULT_OUTPUT_FILENAME = 'webpack-stats.json';
var DEFAULT_LOG_TIME = false;


function Plugin(options) {
  this.contents = {};
  this.options = options || {};
  this.options.filename = this.options.filename || DEFAULT_OUTPUT_FILENAME;
  if (this.options.logTime === undefined) {
    this.options.logTime = DEFAULT_LOG_TIME;
  }
}

Plugin.prototype.apply = function(compiler) {
    var self = this;

    compiler.plugin('compilation', function(compilation, callback) {
      compilation.plugin('failed-module', function(fail){
        var output = {
          status: 'error',
          error: fail.error.name || 'unknown-error'
        };
        if (fail.error.module !== undefined) {
          output.file = fail.error.module.userRequest;
        }
        if (fail.error.error !== undefined) {
          output.message = stripAnsi(fail.error.error.codeFrame);
        }
        self.writeOutput(compiler, output);
      });
    });

    compiler.plugin('compile', function(factory, callback) {
      self.writeOutput(compiler, {status: 'compiling'});
    });

    compiler.plugin('done', function(stats){
      if (stats.compilation.errors.length > 0) {
        var error = stats.compilation.errors[0];
        self.writeOutput(compiler, {
          status: 'error',
          error: error['name'] || 'unknown-error',
          message: stripAnsi(error['message'])
        });
        return;
      }

      var chunks = {};
      stats.compilation.chunks.map(function(chunk){
        var files = chunk.files.map(function(file){
          var F = {name: file};
          if (compiler.options.output.publicPath) {
            F.publicPath= compiler.options.output.publicPath + file;
          }
          if (compiler.options.output.path) {
            F.path = path.join(compiler.options.output.path, file);
          }
          return F;
        });
        chunks[chunk.name] = files;
      });
      var output = {
        status: 'done',
        chunks: chunks
      };

      if (self.options.logTime === true) {
        output.startTime = stats.startTime;
        output.endTime = stats.endTime;
      }

      self.writeOutput(compiler, output);
    });
};


Plugin.prototype.writeOutput = function(compiler, contents) {
  var outputDir = this.options.path || '.';
  var outputFilename = path.join(outputDir, this.options.filename || DEFAULT_OUTPUT_FILENAME);
  if (compiler.options.output.publicPath) {
    contents.publicPath = compiler.options.output.publicPath;
  }
  mkdirp.sync(path.dirname(outputFilename));

  this.contents = extend(this.contents, contents);
  fs.writeFileSync(
    outputFilename,
    JSON.stringify(this.contents, null, this.options.indent)
  );
};

module.exports = Plugin;


/***/ }),

/***/ 1342:
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* WEBPACK VAR INJECTION */(function(Buffer) {/*!
 * @description Recursive object extending
 * @author Viacheslav Lotsmanov <lotsmanov89@gmail.com>
 * @license MIT
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2013-2015 Viacheslav Lotsmanov
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */



function isSpecificValue(val) {
	return (
		val instanceof Buffer
		|| val instanceof Date
		|| val instanceof RegExp
	) ? true : false;
}

function cloneSpecificValue(val) {
	if (val instanceof Buffer) {
		var x = new Buffer(val.length);
		val.copy(x);
		return x;
	} else if (val instanceof Date) {
		return new Date(val.getTime());
	} else if (val instanceof RegExp) {
		return new RegExp(val);
	} else {
		throw new Error('Unexpected situation');
	}
}

/**
 * Recursive cloning array.
 */
function deepCloneArray(arr) {
	var clone = [];
	arr.forEach(function (item, index) {
		if (typeof item === 'object' && item !== null) {
			if (Array.isArray(item)) {
				clone[index] = deepCloneArray(item);
			} else if (isSpecificValue(item)) {
				clone[index] = cloneSpecificValue(item);
			} else {
				clone[index] = deepExtend({}, item);
			}
		} else {
			clone[index] = item;
		}
	});
	return clone;
}

/**
 * Extening object that entered in first argument.
 *
 * Returns extended object or false if have no target object or incorrect type.
 *
 * If you wish to clone source object (without modify it), just use empty new
 * object as first argument, like this:
 *   deepExtend({}, yourObj_1, [yourObj_N]);
 */
var deepExtend = module.exports = function (/*obj_1, [obj_2], [obj_N]*/) {
	if (arguments.length < 1 || typeof arguments[0] !== 'object') {
		return false;
	}

	if (arguments.length < 2) {
		return arguments[0];
	}

	var target = arguments[0];

	// convert arguments to array and cut off target object
	var args = Array.prototype.slice.call(arguments, 1);

	var val, src, clone;

	args.forEach(function (obj) {
		// skip argument if it is array or isn't object
		if (typeof obj !== 'object' || Array.isArray(obj)) {
			return;
		}

		Object.keys(obj).forEach(function (key) {
			src = target[key]; // source value
			val = obj[key]; // new value

			// recursion prevention
			if (val === target) {
				return;

			/**
			 * if new value isn't object then just overwrite by new value
			 * instead of extending.
			 */
			} else if (typeof val !== 'object' || val === null) {
				target[key] = val;
				return;

			// just clone arrays (and recursive clone objects inside)
			} else if (Array.isArray(val)) {
				target[key] = deepCloneArray(val);
				return;

			// custom cloning and overwrite for specific objects
			} else if (isSpecificValue(val)) {
				target[key] = cloneSpecificValue(val);
				return;

			// overwrite by new value if source isn't object or array
			} else if (typeof src !== 'object' || src === null || Array.isArray(src)) {
				target[key] = deepExtend({}, val);
				return;

			// source value and new value is objects both, extending...
			} else {
				target[key] = deepExtend(src, val);
				return;
			}
		});
	});

	return target;
}

/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(2).Buffer))

/***/ }),

/***/ 1343:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

module.exports = function () {
	return /(?:(?:\u001b\[)|\u009b)(?:(?:[0-9]{1,3})?(?:(?:;[0-9]{0,3})*)?[A-M|f-m])|\u001b[A-M]/g;
};


/***/ }),

/***/ 1344:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var ansiRegex = __webpack_require__(1343)();

module.exports = function (str) {
	return typeof str === 'string' ? str.replace(ansiRegex, '') : str;
};


/***/ })

})
//# sourceMappingURL=0.8a6b57b3d2511838e3a3.hot-update.js.map