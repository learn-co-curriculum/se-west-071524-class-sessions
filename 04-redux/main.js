import './style.css'
import { legacy_createStore as createStore } from 'redux'


const initialState = {
  budget: 200,
  pets: [
    {id: 1, name: "Daisy", species: "dog"},
    {id: 2, name: "Felix", species: "cat"}
  ]
}

function reducer(currState=initialState, action){
  switch (action.type) {
    case "addTen":
      // currState.budget += 10 // direct state mutation allowed!
      return {
        ...currState,
        budget: currState.budget += 10
      }
      case "subtractTen":
        return {
              ...currState,
              budget: currState.budget -= 10
            }
        case "subtractAmount":
          return {
            ...currState,
            budget: currState.budget -= action.payload
          }
        case "addPet":
          return {
            ...currState,
            pets: [...currState.pets, action.payload]
          }
    default:
      return currState
  }
  // if (action.type == "addTen") {
  //   return {
  //     ...currState,
  //     budget: currState.budget += 10
  //   }
  // } else if (action.type == "subtractTen") {
  //   return {
  //     ...currState,
  //     budget: currState.budget -= 10
  //   }
  // }
  // return currState
  
}

const store = createStore(reducer)
console.log("🚀 ~ store:", store)
console.log("🚀 ~ store:", store.getState())

store.subscribe(() => {
  const state = store.getState()
  const budgetH3 = document.querySelector("#budget")
  budgetH3.textContent = `Budget: ${state.budget}`
  const petsUl = document.querySelector('#pets')
  petsUl.innerHTML = ""
  state.pets.forEach(p => {
    const li = document.createElement('li')
    li.textContent = `Name: ${p.name} | Species: ${p.species}`
    petsUl.append(li)
  })
})

const addTenAction = {
  type: "addTen"
}

const subtractTen = { type: "subtractTen"}

const subtractAction = { type: "subtractAmount", payload: 5} // hardcoding 5 for demo purposes

// store.dispatch({ type: "bananas"})
store.dispatch(addTenAction) // calls the reducer()
store.dispatch(addTenAction) // calls the reducer()
store.dispatch(subtractTen)
console.log("🚀 ~ store:", store.getState())

const addBtn = document.querySelector("#add10")
const subBtn = document.querySelector("#subtract")
const removeBtn = document.querySelector("#removeAmt")

addBtn.addEventListener("click", () => store.dispatch(addTenAction))
subBtn.addEventListener("click", () => store.dispatch(subtractAction))
removeBtn.addEventListener("click", (e) => {
  const removeAmount = Number(document.querySelector("#subAmt").value)
  console.log("🚀 ~ removeBtn.addEventListener ~ removeAmount:", removeAmount)
  store.dispatch({ type: "subtractAmount", payload: removeAmount })
})

store.dispatch({ type: "addPet", payload: {id: 3, name: "Zeus", species: 'dog'}})

