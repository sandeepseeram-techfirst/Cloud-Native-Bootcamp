
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;


contract NoteApp{

    // create a state variable to hold message
    string public note;

    // Constructor function initializes the state variable with initial message
    constructor(string memory _note) { 
        note = _note;
    }

    // Function to read message
    function viewMyNote() public view returns (string memory) {
        return note;
    }

    // Function to set a new message
    function setNote(string memory _note) public {
        note = _note;
    }
}
