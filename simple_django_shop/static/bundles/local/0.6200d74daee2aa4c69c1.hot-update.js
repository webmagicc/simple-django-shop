webpackHotUpdate(0,{

/***/ 553:
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function(module) {/* REACT HOT LOADER */ if (true) { (function () { var ReactHotAPI = __webpack_require__(351), RootInstanceProvider = __webpack_require__(352), ReactMount = __webpack_require__(144), React = __webpack_require__(12); module.makeHot = module.hot.data ? module.hot.data.makeHot : ReactHotAPI(function () { return RootInstanceProvider.getRootInstances(ReactMount); }, React); })(); } try { (function () {

"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _searchkit = __webpack_require__(63);

var _searchkit2 = _interopRequireDefault(_searchkit);

var _react = __webpack_require__(12);

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(38);

var _reactDom2 = _interopRequireDefault(_reactDom);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var host = "http://demo.searchkit.co/api/movies";
var sk = new _searchkit2.default.SearchkitManager(host, {});
var Hits = _searchkit2.default.Hits;

var MovieHit = function (_React$Component) {
  _inherits(MovieHit, _React$Component);

  function MovieHit() {
    _classCallCheck(this, MovieHit);

    return _possibleConstructorReturn(this, (MovieHit.__proto__ || Object.getPrototypeOf(MovieHit)).apply(this, arguments));
  }

  _createClass(MovieHit, [{
    key: "render",
    value: function render() {
      var result = this.props.result;
      var url = "http://www.imdb.com/title/" + result._source.imdbId;
      return _react2.default.createElement(
        "div",
        { className: this.props.bemBlocks.item().mix(this.props.bemBlocks.container("item")), key: result._id },
        _react2.default.createElement(
          "a",
          { href: url, target: "_blank" },
          _react2.default.createElement("img", { className: this.props.bemBlocks.item("poster"), src: result._source.poster, width: "100", height: "140" }),
          _react2.default.createElement(
            "div",
            { className: this.props.bemBlocks.item("title") },
            result._source.title
          )
        )
      );
    }
  }]);

  return MovieHit;
}(_react2.default.Component);

var SearchkitProvider = _searchkit2.default.SearchkitProvider;
var Searchbox = _searchkit2.default.SearchBox;

var Application = function (_React$Component2) {
  _inherits(Application, _React$Component2);

  function Application() {
    _classCallCheck(this, Application);

    return _possibleConstructorReturn(this, (Application.__proto__ || Object.getPrototypeOf(Application)).apply(this, arguments));
  }

  _createClass(Application, [{
    key: "render",
    value: function render() {

      return _react2.default.createElement(
        "div",
        null,
        _react2.default.createElement(
          SearchkitProvider,
          { searchkit: sk },
          _react2.default.createElement(
            "div",
            { className: "search" },
            _react2.default.createElement(
              "div",
              { className: "search__query" },
              _react2.default.createElement(Searchbox, { searchOnChange: true, prefixQueryFields: ["actors^1", "type^2", "languages", "title^10"] })
            ),
            _react2.default.createElement(
              "div",
              { className: "search__results" },
              _react2.default.createElement(Hits, { hitsPerPage: 6, itemComponent: MovieHit })
            )
          )
        )
      );
    }
  }]);

  return Application;
}(_react2.default.Component);

_reactDom2.default.render(_react2.default.createElement(Application, null), document.getElementById('app'));

/* REACT HOT LOADER */ }).call(this); } finally { if (true) { (function () { var foundReactClasses = module.hot.data && module.hot.data.foundReactClasses || false; if (module.exports && module.makeHot) { var makeExportsHot = __webpack_require__(353); if (makeExportsHot(module, __webpack_require__(12))) { foundReactClasses = true; } var shouldAcceptModule = true && foundReactClasses; if (shouldAcceptModule) { module.hot.accept(function (err) { if (err) { console.error("Cannot apply hot update to " + "Main.js" + ": " + err.message); } }); } } module.hot.dispose(function (data) { data.makeHot = module.makeHot; data.foundReactClasses = foundReactClasses; }); })(); } }
/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(145)(module)))

/***/ })

})
//# sourceMappingURL=0.6200d74daee2aa4c69c1.hot-update.js.map