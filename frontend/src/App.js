import React, {Component} from "react";
import { Container, Row, Col } from "reactstrap"
import ModalForm from './Components/Modals/ModalForm'
import MoviesTable from './Components/Tables/MoviesTable'
import MoviesBackend from "./Repository/MoviesBackend";

class App extends Component {
  state = {
    items: [],
    totalItems: 0
  }

  /**
   * Adds a new item to the state.
   *
   * @param {*} item
   */
  addItemToState = (item) => {
    this.setState(prevState => ({...prevState, items: [...prevState.items, item]}))
  }

  setTotalItems = (response) => {
    this.setState({...this.state, totalItems: response.headers.get('x-total-count')})

    return response
  }

  /**
   * Updates one of the items in the state.
   *
   * @param {*} item
   */
  updateState = (item) => {
    const itemIndex = this.state.items.findIndex(data => data.id === item.id)

    this.setState({ ...this.state, items: [...this.state.items.slice(0, itemIndex), item, ...this.state.items.slice(itemIndex + 1)] })
  }

  /**
   * Deletes an item from the state.
   *
   * @param {*} id
   */
  deleteItemFromState = (id) => {
    this.setState({ ...this.state, items: this.state.items.filter(item => item.id !== id) })
  }

  componentDidMount() {
    MoviesBackend.getItems()
      .then((response) => this.setTotalItems(response))
      .then((response) => response.json())
      .then((items) => this.setState({...this.state, items}))
      .catch((err) => console.error('getItems', err))
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
            <ModalForm buttonLabel="Add item" addItemToState={this.addItemToState} />
          </Col>
        </Row>
        <Row>
          <Col>
            <MoviesTable
              items={this.state.items}
              updateState={this.updateState}
              deleteItemFromState={this.deleteItemFromState}
            />
          </Col>
        </Row>
      </Container>
    )
  }
}

export default App
