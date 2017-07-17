import Searchkit from "searchkit";
import {
  InitialLoader,
  NoHits,
  Pagination,
  Layout,
  TopBar,
  LayoutBody,
  SideBar,
  HierarchicalMenuFilter,
  RefinementListFilter,
  LayoutResults,
  ActionBar,
  ActionBarRow,
  HitsStats,
  ViewSwitcherHits,
  ViewSwitcherToggle,
  SearchBox,
  SelectedFilters,
  ResetFilters
} from "searchkit";

import React from "react";
import ReactDOM from "react-dom";

//const host = "http://demo.searchkit.co/api/movies"
const host = "http://localhost:9200/products/" + window.category
const sk = new Searchkit.SearchkitManager(host, {})
const Hits = Searchkit.Hits


class MovieHit extends React.Component {
  
  render() {
    const result = this.props.result;
        let url = '/' + window.category + '/' + result._source.slug
        let img = 'http://fabro.com.ua' + result._source.image
        return (
            <div className={this.props.bemBlocks.item().mix(this.props.bemBlocks.container("item")) + " col s12 m4"} key={result._id}>
                <a href={url} target="_blank">
                    <img className={this.props.bemBlocks.item("poster")} src={img} width="200" />
                    <div className={this.props.bemBlocks.item("title")}>{result._source.name}</div>
                </a>
            </div>
        )
    }
  
}
const SearchkitProvider = Searchkit.SearchkitProvider;
const Searchbox = Searchkit.SearchBox;
class Application extends React.Component {
  render() {
   
    
    return (<div>
      
      <SearchkitProvider searchkit={sk}>
        <Layout>
          <LayoutBody>
            <SideBar>
              <RefinementListFilter
                field="brand"
                title="Производитель"
                operator="AND"
                id="brand"/>
              <RefinementListFilter
                id="emkost-akkumulyatora-mach"
                title="Емкость аккумулятора, мАч"
                field="emkost-akkumulyatora-mach"
                operator="AND"
                size={10}/>
            </SideBar>
            <LayoutResults>
              <SearchBox
              autofocus={true}
              searchOnChange={true}
              prefixQueryFields={["name^1"]}/>
              <ActionBar>
                <ActionBarRow>
                  <HitsStats/>
                </ActionBarRow>
                <ActionBarRow>
                  <SelectedFilters/>
                  <ResetFilters/>
                </ActionBarRow>
              </ActionBar>
              <Hits hitsPerPage={60} itemComponent={MovieHit}/>
              <NoHits/>
              <div className="clearfix"></div>
              <div className="row">
                <Pagination showNumbers={true}/>
              </div>
              </LayoutResults>
          </LayoutBody>
         </Layout>
      </SearchkitProvider>

    </div>);
  }
}


ReactDOM.render(
  <Application />,
  document.getElementById('app')
);