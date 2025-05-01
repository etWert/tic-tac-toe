import React, { useState } from 'react'
import './board.css'
const Board = () => {
    const [cells, setCells] = useState(Array(9).fill(null));
    const [sign, setSign] = useState('X')

    const handleOnClick = (index) => {
        //סימון התא
        if (cells[index] !== null) {
            return;//תא תפוס
        }
        else {
            const newCells = [...cells]
            newCells[index] = sign
            setCells(newCells)
        }
        if (sign === 'X')
            setSign('O')
        else
            setSign('X')
    }
    return (
        <div className='board'>
            {cells.map((cell, index) => (
                <div key={index} className="cell" onClick={() => handleOnClick(index)}>{cell}</div>

            ))}
        </div>
    )
}

export default Board