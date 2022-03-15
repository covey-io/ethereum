function generateNewAccounts(password, numberOfAccounts) {
    const newAccount = personal.newAccount(password);
    console.log(newAccount);

    for (let index = 0; index < numberOfAccounts; index++) {
        const newAccount = personal.newAccount(password);
        console.log(newAccount);
    }
}
