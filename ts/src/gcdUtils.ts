function recursiveGCD(a: number, b: number) : number {
    if (a < 0 || b < 0) {
        throw new Error("Both numbers have to be >= 0");
    }

    return recursiveGCDHelper(a, b);
}

function recursiveGCDHelper(a: number, b: number) : number {
    return a ===  0 ? b : recursiveGCDHelper(b % a,  a);
}

function gcd(a: number, b: number) : number {
    if (a < 0 || b < 0) {
        throw new Error("Both numbers have to be >= 0");
    }

    while (a !== 0) { 
        let temp : number =  a
        a = b % a;
        b = temp;
    }

    return b;
}

export {recursiveGCD, gcd};
