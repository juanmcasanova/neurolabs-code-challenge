import { Component } from 'react';
import {Button, Modal, ModalHeader, ModalBody, ModalFooter} from 'reactstrap';

class ConfirmationModal extends Component {
  constructor(props) {
    super(props)

    this.state = {
      modal: false
    }
  }

  toggle = () => {
    this.setState(prevState => ({
      modal: !prevState.modal
    }))
  }

  render() {
    return (
      <span>
        <Button color="danger" onClick={this.toggle}>Delete</Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader>Delete item?</ModalHeader>

          <ModalBody>This operation cannot be undone. Are you sure you wish to delete the movie #{this.props.item.id} {this.props.item.title}?</ModalBody>

          <ModalFooter>
            <Button onClick={this.toggle}>Cancel</Button>
            <Button color="danger" variant="primary" onClick={() => this.props.deleteItem(this.props.item)}>Delete</Button>
          </ModalFooter>
        </Modal>
      </span>
    );
  }
}

export default ConfirmationModal;
