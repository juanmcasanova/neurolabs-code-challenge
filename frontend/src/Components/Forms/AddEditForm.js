import React from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import MoviesBackend from '../../Repository/MoviesBackend';

class AddEditForm extends React.Component {
  state = {
    id: 0,
    title: ''
  }

  onChange = (e) => {
    this.setState({[e.target.name]: e.target.value})
  }

  submitFormAdd = (e) => {
    e.preventDefault()
    MoviesBackend.addItem(this.state.title)
      .then((item) => {
        this.props.addItemToState(item)
        this.props.toggle()
      })
      .catch(err => console.err(err))
  }

  submitFormEdit = (e) => {
    e.preventDefault()
    MoviesBackend.editItem(this.state.id, this.state.title)
      .then((item) => {
        this.props.updateState(item)
        this.props.toggle()
      })
      .catch(err => console.err(err))
  }

  componentDidMount(){
    // If item exists, populate the state with proper data
    if(this.props.item) {
      const { id, title } = this.props.item
      this.setState({ id, title })
    }
  }

  render() {
    return (
      <Form onSubmit={this.props.item ? this.submitFormEdit : this.submitFormAdd}>
        <FormGroup>
          <Label for="title">Title</Label>
          <Input type="text" name="title" id="title" onChange={this.onChange} value={this.state.title === null ? '' : this.state.title} />
        </FormGroup>
        <Button>Submit</Button>
      </Form>
    );
  }
}

export default AddEditForm
