import React from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import { BACKEND_BASE_PATH } from "../../constants";

class AddEditForm extends React.Component {
  state = { id, title }

  onChange = (e) => {
    this.setState({[e.target.name]: e.target.value})
  }

  submitFormAdd = (e) => {
    e.preventDefault()
    fetch(BACKEND_BASE_PATH+'/movies', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title: this.state.title })
    })
      .then((response) => response.json())
      .then((item) => {
        this.props.addItemToState(item)
        this.props.toggle()
      })
      .catch(err => console.err(err))
  }

  submitFormEdit = (e) => {
    e.preventDefault()
    fetch(BACKEND_BASE_PATH+'/movies/'+this.state.id, {
      method: 'put',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title: this.state.title })
    })
      .then((response) => response.json())
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
