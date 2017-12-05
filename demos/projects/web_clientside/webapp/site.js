function runAtLoadButOnce() {
    const person = "Jeff";
    console.log("Nice to meet you " + person)

    let p = new Person('Tom', 11);
    let p2 = new Person('Jake', 14)
    console.log(p.name + " is " + p.age + " years old")
}

runAtLoadButOnce()

