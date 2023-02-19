import React, {Component} from "react";
import { Table } from "reactstrap";
import ModalForm from '../Modals/ModalForm'
import ConfirmationModal from "../Modals/ConfirmationModal";
import MoviesBackend from "../../Repository/MoviesBackend";

class MoviesTable extends Component {
    /**
     * Deletes a movie from the database and the state.
     *
     * @param {*} item
     */
    deleteItem = (item) => {
        MoviesBackend.deleteItem(item)
            .then(() => {this.props.deleteItemFromState(item.id)})
            .catch(err => console.error(err))
    }

    /**
     * Returns the actual component markup.
     */
    render() {
        const items = this.props.items.map(item => {
            return (
                <tr key={item.id}>
                    <th scope="row">{item.id}</th>
                    <td>{item.title}</td>
                    <td>
                        <ModalForm buttonLabel="Edit" item={item} updateState={this.props.updateState} />
                        <ConfirmationModal item={item} deleteItem={this.deleteItem} />
                    </td>
                </tr>
            )
        })

        return (
            <Table responsive hover>
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
