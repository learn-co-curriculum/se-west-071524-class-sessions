// import { useState } from 'react'
import Budget from './components/Budget'
import PetBrowser from './components/PetBrowser'
import DogBrowser from './components/DogBrowser'
import './App.css'

function App() {

  return (
    <div className="App">
      <header className='App-header'>
        <h1>Redux Shelter</h1>
      </header>
      <Budget />
      <PetBrowser />
    </div>
  )
}

export default App
