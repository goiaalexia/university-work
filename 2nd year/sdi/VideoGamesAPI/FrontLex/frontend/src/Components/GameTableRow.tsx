import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';


export default function GameTableRow(props: any) {
    let { game_avg_year, id,description, name, releaseYear, company, rating, sales, platform } = props.object
    const [platformName, setName] = useState("")

    useEffect(() => {
        fetch(process.env.REACT_APP_API_URL + "/platforms/" + platform + "/")
            .then(response => response.json())
            .then(data => setName(data["name"]))
    }, [])

    const handleClick = (e: any) => {
        e.preventDefault()
        props.onClick({ game_avg_year, id, description,name, releaseYear, company, rating, sales, platform })
    }

    const handleDelete = (e: any) => {
        e.preventDefault() // don't delete the entire database vibezz
        props.deleteGame(id)
    }

    return (
        <tr key={id} onClick={handleClick}>
            {props.onFilter ? <td>{game_avg_year}</td> : null}
            <td>{name}</td>
            <td>{description}</td>
            <td>{releaseYear}</td>
            <td>{company}</td>
            <td>{rating}</td>
            <td>{sales}</td>
            <td>{platformName}</td>
            {!props.noDelete ? <td><Button  className="p-2 my-2 w-100 btn-danger" onClick={handleDelete}>Delete</Button></td> : null}
        </tr>
    );
}



