import React, {useEffect, useRef, useState} from 'react';
import CustomNavbar from "../Components/Navbar";
import Container from 'react-bootstrap/Container';
import {Alert, Button, Col, Form, Pagination, Row, Stack, Table} from 'react-bootstrap';
import GameTableRow from '../Components/GameTableRow';

export interface Game {
    id: string,
    name: string,
    releaseYear: string,
    company: string,
    rating: string,
    sales: string,
    platform: string
}

export default function VideoGames() {
    const [data, setData] = useState<Game[]>([])
    const [selection, setSelection] = useState<Game | undefined>({} as Game)

    const form = useRef(null)

    const endpoint = "/videogames/"
    const fetchData = (page: number) => {
        fetch(process.env.REACT_APP_API_URL + endpoint + "?page=" + page, {})
            .then(response => response.json())
            .then(json => {
                setData(json.videogames)
                setLast(json["last_page"])
            })
    }
    useEffect(() => {
        console.log(page)
        fetchData(1)

    }, [])

    const selectGame = (dt: any) => {
        console.log(dt)
        setSelection(dt)
    }

    const [page, setPage] = useState(1)
    const [lastPage, setLast] = useState(10)

    const changePage = (nr: number) => {
        nr = Math.min(Math.max(nr, 1), lastPage);
        setPage(nr)
        fetchData(nr)
    }

    const [response, setResponse] = useState("")
    const [isOk, setOk] = useState(true)

    const showAlert = (alert: any, ok: boolean) => {
        setResponse("Response: " + alert)
        setOk(ok)
        setTimeout(() => {
            setResponse("")
            setOk(true)
        }, 3000)
    }

    const update = (e: any) => {
        e.preventDefault()
        if (selection == undefined)
            return
        console.log(selection)
        fetch(process.env.REACT_APP_API_URL + endpoint + (selection!.id ? selection!.id+"/" : ""), {
            method: selection!.id ? "PUT" : "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(selection),
        }).then(response => {
            showAlert("[" + response.status + "] " + response.statusText, (400 <= response.status && response.status < 600) ? false : true)
        })
            .then(() => {
                fetchData(page)
            })
    }

    const deleteGame = (id: any) => {
        if (id) {
            fetch(process.env.REACT_APP_API_URL + "/videogames/" + id + "/", {
                method: "DELETE"
            }).then(response => console.log(response))
                .then(() => {
                    fetchData(page)
                    showAlert("Delete successful", true)

                })
        }
    }

    const clearSelection = () => {
        setSelection(undefined)
    }


    let [direction, setDir] = useState(true)
    const handleSort = () => {
        let temp = [...data]

        console.log(temp)
        temp.sort((a: Game, b: Game) => {
            return a.name.localeCompare(b.name)
        })
        setData(direction ? temp : temp.reverse())
        setDir(!direction)
    }

    return (
        <>
            <CustomNavbar/>
            <Container fluid className="pt-5">
                <Form className='my-3' ref={form}>
                    <Container>
                        <Row>
                            <Col md={12} lg={6}>
                                <Form.Group className="mb-3" controlId="formId">
                                    <Form.Label>Id:</Form.Label>
                                    <Form.Control value={selection ? selection!.id : ""} type="text" placeholder=""
                                                  disabled readOnly/>
                                </Form.Group>
                            </Col>
                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formName">
                                    <Form.Label>Name:</Form.Label>
                                    <Form.Control value={selection ? selection!.name : ""}
                                                  onChange={e => setSelection({...selection!, name: e.target.value})}
                                                  type="text" placeholder=""/>
                                </Form.Group>
                            </Col>
                        </Row>

                        <Row>
                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formReleaseYear">
                                    <Form.Label>Release Year:</Form.Label>
                                    <Form.Control value={selection ? selection!.releaseYear : ""}
                                                  onChange={e => setSelection({
                                                      ...selection!,
                                                      releaseYear: e.target.value
                                                  })} type="text" placeholder=""/>
                                </Form.Group>
                            </Col>

                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formCompany">
                                    <Form.Label>Company:</Form.Label>
                                    <Form.Control value={selection ? selection!.company : ""}
                                                  onChange={e => setSelection({...selection!, company: e.target.value})}
                                                  type="text" placeholder=""/>
                                </Form.Group>
                            </Col>
                        </Row>

                        <Row>
                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formRating">
                                    <Form.Label>Rating:</Form.Label>
                                    <Form.Control value={selection ? selection!.rating : ""}
                                                  onChange={e => setSelection({...selection!, rating: e.target.value})}
                                                  type="text" placeholder=""/>
                                </Form.Group>
                            </Col>

                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formSales">
                                    <Form.Label>Sales:</Form.Label>
                                    <Form.Control value={selection ? selection!.sales : ""}
                                                  onChange={e => setSelection({...selection!, sales: e.target.value})}
                                                  type="text" placeholder=""/>
                                </Form.Group>
                            </Col>
                        </Row>

                        <Row>
                            <Col md={12} lg={6}>
                                <Form.Group className="mb-1" controlId="formPlatform">
                                    <Form.Label>Platform Id:</Form.Label>
                                    <Form.Control value={selection ? selection!.platform : ""}
                                                  onChange={e => setSelection({
                                                      ...selection!,
                                                      platform: e.target.value
                                                  })} type="text" placeholder=""/>
                                </Form.Group>
                            </Col>


                        </Row>

                        <Row className='my-3'>
                            <Col sm={12}>
                                <Alert
                                    variant={response == "" ? "primary" : (isOk ? "success" : "danger")}>{response == "" ? "Response: " : response}</Alert>
                            </Col>
                        </Row>

                        <Row>
                            <Col md={12} lg={6}>
                                <Button type="submit" className="p-2 my-2 w-100" onClick={update}>Modify</Button>
                            </Col>

                            <Col md={12} lg={6}>
                                <Button className="p-2 my-2 w-100 btn-danger" onClick={clearSelection}>Clear</Button>
                            </Col>
                        </Row>
                    </Container>
                </Form>
                <Stack className='w-100 mx-auto' direction="horizontal">
                    <Pagination className='w-100 mx-auto d-flex justify-content-center'>
                        <Pagination.Prev onClick={() => {
                            changePage(page - 1)
                        }}/>
                        <Pagination.Item active={page == 1} onClick={() => {
                            changePage(1)
                        }}>{1}</Pagination.Item>
                        {page > 3 ? <Pagination.Ellipsis/> : null}
                        {page > 2 ? <Pagination.Item className="d-none d-lg-block" onClick={() => {
                            changePage(page - 1)
                        }}>{page - 1}</Pagination.Item> : null}


                        {page > 1 && page < lastPage ? <Pagination.Item active onClick={() => {
                            changePage(page)
                        }}>{page}</Pagination.Item> : null}

                        {page < lastPage - 1 ? <Pagination.Item className="d-none d-lg-block" onClick={() => {
                            changePage(page + 1)
                        }}>{page + 1}</Pagination.Item> : null}
                        {page < lastPage - 2 ? <Pagination.Ellipsis/> : null}
                        <Pagination.Item active={page == lastPage} onClick={() => {
                            changePage(lastPage)
                        }}>{lastPage}</Pagination.Item>
                        <Pagination.Next onClick={() => {
                            changePage(page + 1)
                        }}/>
                    </Pagination>
                </Stack>

                <Table responsive hover>
                    <thead>
                    <tr>
                        <th onClick={handleSort}>Name</th>
                        <th>Description</th>
                        <th onClick={() => {
                            changePage(page + 1)
                        }}>Release Year
                        </th>
                        <th>Company</th>
                        <th>Rating</th>
                        <th>Sales</th>
                        <th>Platform</th>
                    </tr>
                    </thead>
                    <tbody>
                    {data ? data.map((e: Game) =>
                        <GameTableRow key={e.id} object={e} onClick={selectGame} deleteGame={deleteGame}/>
                    ) : null}
                    </tbody>
                </Table>
            </Container>
        </>
    );
}
