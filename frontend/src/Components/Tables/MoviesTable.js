import React, {Component} from "react";
import { Table, Button } from "reactstrap";
import ModalForm from '../Modals/Modal'

class MoviesTable extends Component {
    deleteItem = id => {
        let confirmDelete = window.confirm('Delete item forever?')
        if (confirmDelete) {
            fetch('http://localhost:8000/movies/'+id, { method: 'delete' })
            // @todo Not needed?
            .then(response => response.json())
            .then(item => {
                this.props.deleteItemFromState(id)
            })
            .catch(err => console.error(err))
        }
    }

    render() {
        const items = this.props.items.map(item => {
            return (
                <tr key={item.id}>
                    <th scope="row">{item.id}</th>
                    <td>{item.title}</td>
                    <td>
                        <div style={{width: "110px"}}>
                            <ModalForm buttonLabel="Edit" item={item} updateState={this.props.updateState} />
                            {' '}
                            <Button color="danger" onClick={() => this.deleteItem(item.id)}>Delete</Button>
                        </div>
                    </td>
                </tr>
            )
        })

        return (
            <Table response hover>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>{items}</tbody>
            </Table>
        )
    }
}

export default MoviesTable
