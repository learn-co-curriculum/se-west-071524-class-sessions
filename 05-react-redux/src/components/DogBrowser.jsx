import React, { useState } from 'react'
// import { useFetchBreedsQuery } from '../app/services/dogsApiSlice';


export default function DogBrowser() {

    const [numDogs, setNumDogs] = useState(10);

    // const { data=[], isFetching } = useFetchBreedsQuery(numDogs)
    const data = []

    return (
        <div>
            <h1>Browse Dogs by Breed</h1>
            <div>
                <p>Dogs to fetch:</p>
                <select value={numDogs} onChange={(e) => setNumDogs(Number(e.target.value))}>
                    <option value="5">5</option>
                    <option value="10">10</option>
                    <option value="15">15</option>
                    <option value="20">20</option>
                </select>
            </div>
            <div>
                <p>Number of dogs fetched: {data.length}</p>
                <table>
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th>Picture</th>
                    </tr>
                    </thead>
                    <tbody>
                    {data.map(breed => (
                        <tr key={breed.id}>
                        <td>{breed.name}</td>
                        <td>
                            <img src={breed.image.url} alt={breed.name} height={250}/>
                        </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}
