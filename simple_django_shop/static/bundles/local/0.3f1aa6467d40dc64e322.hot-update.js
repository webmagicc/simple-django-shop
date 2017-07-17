webpackHotUpdate(0,{

/***/ 522:
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function(module) {/* REACT HOT LOADER */ if (true) { (function () { var ReactHotAPI = __webpack_require__(306), RootInstanceProvider = __webpack_require__(307), ReactMount = __webpack_require__(134), React = __webpack_require__(1); module.makeHot = module.hot.data ? module.hot.data.makeHot : ReactHotAPI(function () { return RootInstanceProvider.getRootInstances(ReactMount); }, React); })(); } try { (function () {

"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _searchkit = __webpack_require__(50);

var _searchkit2 = _interopRequireDefault(_searchkit);

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(28);

var _reactDom2 = _interopRequireDefault(_reactDom);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

//const host = "http://demo.searchkit.co/api/movies"
var host = "http://localhost:9200/products";
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
      var url = "/tablets/" + result._source.slug;
      return _react2.default.createElement(
        "div",
        { className: this.props.bemBlocks.item().mix(this.props.bemBlocks.container("item")) + " col s12 m4", key: result._id },
        _react2.default.createElement(
          "a",
          { href: url, target: "_blank" },
          _react2.default.createElement("img", { className: this.props.bemBlocks.item("poster"), src: result._source.image, width: "200" }),
          _react2.default.createElement(
            "div",
            { className: this.props.bemBlocks.item("title") },
            result._source.name
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
            _searchkit.Layout,
            null,
            _react2.default.createElement(
              _searchkit.LayoutBody,
              null,
              _react2.default.createElement(
                _searchkit.SideBar,
                null,
                _react2.default.createElement(_searchkit.RefinementListFilter, {
                  field: "brand",
                  title: "\u041F\u0440\u043E\u0438\u0437\u0432\u043E\u0434\u0438\u0442\u0435\u043B\u044C",
                  operator: "AND",
                  id: "brand" }),
                _react2.default.createElement(_searchkit.RefinementListFilter, {
                  id: "emkost-akkumulyatora-mach",
                  title: "\u0415\u043C\u043A\u043E\u0441\u0442\u044C \u0430\u043A\u043A\u0443\u043C\u0443\u043B\u044F\u0442\u043E\u0440\u0430, \u043C\u0410\u0447",
                  field: "emkost-akkumulyatora-mach",
                  operator: "AND",
                  size: 10 })
              ),
              _react2.default.createElement(
                _searchkit.LayoutResults,
                null,
                _react2.default.createElement(_searchkit.SearchBox, {
                  autofocus: true,
                  searchOnChange: true,
                  prefixQueryFields: ["name^1"] }),
                _react2.default.createElement(
                  _searchkit.ActionBar,
                  null,
                  _react2.default.createElement(
                    _searchkit.ActionBarRow,
                    null,
                    _react2.default.createElement(_searchkit.HitsStats, null)
                  ),
                  _react2.default.createElement(
                    _searchkit.ActionBarRow,
                    null,
                    _react2.default.createElement(_searchkit.SelectedFilters, null),
                    _react2.default.createElement(_searchkit.ResetFilters, null)
                  )
                ),
                _react2.default.createElement(Hits, { hitsPerPage: 60, itemComponent: MovieHit }),
                _react2.default.createElement(_searchkit.NoHits, null),
                _react2.default.createElement("div", { className: "clearfix" }),
                _react2.default.createElement(
                  "div",
                  { className: "row" },
                  _react2.default.createElement(_searchkit.Pagination, { showNumbers: true })
                )
              )
            )
          )
        )
      );
    }
  }]);

  return Application;
}(_react2.default.Component);

_reactDom2.default.render(_react2.default.createElement(Application, null), document.getElementById('app'));

/* REACT HOT LOADER */ }).call(this); } finally { if (true) { (function () { var foundReactClasses = module.hot.data && module.hot.data.foundReactClasses || false; if (module.exports && module.makeHot) { var makeExportsHot = __webpack_require__(308); if (makeExportsHot(module, __webpack_require__(1))) { foundReactClasses = true; } var shouldAcceptModule = true && foundReactClasses; if (shouldAcceptModule) { module.hot.accept(function (err) { if (err) { console.error("Cannot apply hot update to " + "Main.js" + ": " + err.message); } }); } } module.hot.dispose(function (data) { data.makeHot = module.makeHot; data.foundReactClasses = foundReactClasses; }); })(); } }
/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(135)(module)))

/***/ })

})
//# sourceMappingURL=0.3f1aa6467d40dc64e322.hot-update.js.map