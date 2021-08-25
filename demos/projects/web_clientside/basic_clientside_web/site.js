function runAtPageLoad(message) {
    //let person = "Sarah";
    let person = new Person('Sarah', 'James', 34)

    console.log(person.firstName + ' (age: ' + person.age +
        ') --> Running at startup: ' + message);
}

runAtPageLoad("This is the startup message!");
