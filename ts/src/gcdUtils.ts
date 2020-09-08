export function recursiveGCD(a: number, b: number): number {
    if (a < 0 || b < 0) {
        throw new Error('Both numbers have to be >= 0');
    }

    return recursiveGCDHelper(a, b);
}

function recursiveGCDHelper(a: number, b: number): number {
    return a === 0 ? b : recursiveGCDHelper(b % a, a);
}

export function gcd(a: number, b: number): number {
    if (a < 0 || b < 0) {
        throw new Error('Both numbers have to be >= 0');
    }

    while (a !== 0) {
        let temp: number = a;
        a = b % a;
        b = temp;
    }

    return b;
}

export interface ExtendedGCDReturnValue {
    gcd: number;
    x: number;
    y: number;
}

export function xgcd(a: number, b: number): ExtendedGCDReturnValue {
    if (a < 0 || b < 0) {
        throw new Error('Both numbers have to be >= 0');
    }

    let xprev: number = 0;
    let x: number = 1;
    let yprev: number = 1;
    let y: number = 0;
    let q: number;
    let temp: number;

    while (a !== 0) {
        q = Math.floor(b / a);

        temp = x;
        x = xprev - q * x;
        xprev = temp;

        temp = y;
        y = yprev - q * y;
        yprev = temp;

        temp = a;
        a = b % a;
        b = temp;
    }

    return {
        gcd: b,
        x: xprev,
        y: yprev,
    };
}
