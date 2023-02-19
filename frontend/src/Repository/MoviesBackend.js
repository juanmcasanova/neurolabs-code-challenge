import { BACKEND_BASE_PATH } from "../constants"

class MoviesBackend {
    static getItems() {
        return fetch(BACKEND_BASE_PATH+'/movies')
            .then(response => response.json())
    }

    static deleteItem(item) {
        return fetch(BACKEND_BASE_PATH+'/movies/'+item.id, { method: 'delete' })
    }

    static addItem(title) {
        return fetch(BACKEND_BASE_PATH+'/movies', {
                method: 'post',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title })
            })
            .then((response) => response.json())
    }

    static editItem(id, title) {
        return fetch(BACKEND_BASE_PATH+'/movies/'+id, {
                method: 'put',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title })
            })
            .then((response) => response.json())
    }
}

export default MoviesBackend
