pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract StakingToken is ERC20 {

    constructor(uint256 initialSupply) ERC20("Staking Token","ST"){
        _mint(msg.sender, initialSupply);
    }
}

contract RewardToken is ERC20 {

    constructor(uint256 initialSupply) ERC20("Reward Token","RT"){
        _mint(msg.sender, initialSupply);
    }
}