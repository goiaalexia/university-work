import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';


export default function PlatformTableRow(props: any) {
    let { id, name, description, activeUsers, screen, handheld, size } = props.object
    const handleClick = (e: any) => {
        e.preventDefault()
        props.onClick({  id, name, description, activeUsers, screen, handheld, size })
    }

    const handleDelete = (e: any) => {
        e.preventDefault() // don't delete the entire database vibezz
        props.deletePlatform(id)
    }

    return (
        <tr key={id} onClick={handleClick}>
            {props.onFilter ? <td>{name}</td> : null}
            <td>{description}</td>
            <td>{activeUsers}</td>
            <td>{screen}</td>
            <td>{handheld}</td>
            <td>{size}</td>
            {!props.noDelete ? <td><Button  className="p-2 my-2 w-100 btn-danger" onClick={handleDelete}>Delete</Button></td> : null}
        </tr>
    );
}



