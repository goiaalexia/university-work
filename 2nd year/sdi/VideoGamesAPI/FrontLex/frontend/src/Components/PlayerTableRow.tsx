import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';


export default function PlayerTableRow(props: any) {
    let { id, username, age, description, email, gender, favouriteGenre } = props.object
    const handleClick = (e: any) => {
        e.preventDefault()
        props.onClick({ id, username, age, description, email, gender, favouriteGenre })
    }

    const handleDelete = (e: any) => {
        e.preventDefault() // don't delete the entire database vibezz
        props.deleteGame(id)
    }

    return (
        <tr key={id} onClick={handleClick}>
            {props.onFilter ? <td>{username}</td> : null}
            <td>{age}</td>
            <td>{description}</td>
            <td>{email}</td>
            <td>{gender}</td>
            <td>{favouriteGenre}</td>
            {!props.noDelete ? <td><Button  className="p-2 my-2 w-100 btn-danger" onClick={handleDelete}>Delete</Button></td> : null}
        </tr>
    );
}



