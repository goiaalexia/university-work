import React, { useEffect, useState } from 'react';
import CustomNavbar from "../Components/Navbar";
import { Container, Table } from 'react-bootstrap';
import GameTableRow from '../Components/GameTableRow';

interface Game {
    game_avg_year: string,
    id: string,
    name: string,
    releaseYear: string,
    company: string,
    rating: string,
    sales: string,
    platform: string
}

export default function Filter() {
    const [data, setData] = useState([])
    const fetchData = () => {
        fetch(process.env.REACT_APP_API_URL + "/videogames/by-avg-year")
            .then(response => response.json())
            .then(json => { setData(json) })
    }

    useEffect(() => {
        fetchData()
    }, [])

    return (
        <>
            <CustomNavbar />

            <Container className="pt-5">

                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Average Year</th>
                            <th>Name</th>
                            <th>Release Year</th>
                            <th>Company</th>
                            <th>Rating</th>
                            <th>Sales</th>
                            <th>Platform</th>
                        </tr>

                    </thead>
                    <tbody>
                        {data ? data.map((e: any) =>
                            <GameTableRow onFilter key={e.id} object={e} noDelete />
                        ) : null}
                    </tbody>
                </Table>
            </Container>
        </>
    );
}
