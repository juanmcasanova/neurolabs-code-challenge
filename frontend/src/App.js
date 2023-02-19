import React, {Component} from "react";
import { Container, Row, Col } from "reactstrap"
import ModalForm from './Components/Modals/Modal'
import MoviesTable from './Components/Tables/MoviesTable'
import { BACKEND_BASE_PATH } from "./constants";

class App extends Component {
  state = { items: [] }

  /**
   * Performs the actual fetch that will return all the movies data.
   */
  getItems() {
    fetch(BACKEND_BASE_PATH+'/movies')
      .then(response => response.json())
      .then(items => this.setState({items}))
      .catch(err => console.error('getItems', err))
  }

  /**
   * Adds a new item to the state.
   *
   * @param {*} item
   */
  addItemToState = (item) => {
    this.setState(prevState => ({items: [...prevState.items, item]}))
  }

  /**
   * Updates one of the items in the state.
   *
   * @param {*} item
   */
  updateState = (item) => {
    const itemIndex = this.state.items.findIndex(data => data.id === item.id)

    this.setState({ items: [...this.state.items.slice(0, itemIndex), item, ...this.state.items.slice(itemIndex + 1)] })
  }

  /**
   * Deletes an item from the state.
   *
   * @param {*} id
   */
  deleteItemFromState = (id) => {
    this.setState({ items: this.state.items.filter(item => item.id !== id) })
  }

  componentDidMount() {
    this.getItems()
  }

  /**
   * Returns the actual component markup.
   */
  render() {
    return (
      <Container className="App">
        <Row>
          <Col>
            <h1 style={{margin: "20px 0"}}>Neurolabs code challenge</h1>
          </Col>
        </Row>
        <Row>
          <Col>
            <ModalForm buttonLabel="Add item" addItemToState={this.addItemToState} style={{float: "right"}} />
          </Col>
        </Row>
        <Row>
          <Col>
            <MoviesTable items={this.state.items} updateState={this.updateState} deleteItemFromState={this.deleteItemFromState} />
          </Col>
        </Row>
      </Container>
    )
  }
}

export default App
