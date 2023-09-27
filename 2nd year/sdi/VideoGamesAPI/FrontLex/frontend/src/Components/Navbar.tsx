import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

export default function CustomNavbar() {
    return (

            <Navbar bg="dark" variant="dark" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">SDI Laboratory 5:</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link href="/#/videogames">Video Games</Nav.Link>
                            <Nav.Link href="/#/platforms">Platforms</Nav.Link>
                            <Nav.Link href="/#/players">Players</Nav.Link>
                            <Nav.Link href="/#/savefiles">Savefiles</Nav.Link>


                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>

    );
}
