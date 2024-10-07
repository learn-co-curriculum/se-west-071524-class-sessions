import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { addTen, subtractAmount } from '../features/budget/budgetSlice'

export default function Budget() {

  const budget = useSelector(state => state.budget.value)
  const dispatch = useDispatch()
  

  const handleAddTen = () => dispatch(addTen())

  const handleSubtract = () => console.log("subtract clicked")

  return (
    <div>
        <h2>Redux Shelter Budget:</h2>
        <h3>${budget}</h3>
        <div>
            <button className="ui button" onClick={handleAddTen}>Add $10</button>
            <button className="ui button" onClick={handleSubtract}>Subtract $5</button>
        </div>
    </div>
  )
}
