const greaterThanZeroErrorString: string = 'Both numbers have to be > 0';

export function recursiveGCD(a: number, b: number): number {
    if (a <= 0 || b <= 0) {
        throw new Error(greaterThanZeroErrorString);
    }

    return recursiveGCDHelper(a, b);
}

function recursiveGCDHelper(a: number, b: number): number {
    return a === 0 ? b : recursiveGCDHelper(b % a, a);
}

export function gcd(a: number, b: number): number {
    if (a <= 0 || b <= 0) {
        throw new Error(greaterThanZeroErrorString);
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
    if (a <= 0 || b <= 0) {
        throw new Error('Both numbers have to be > 0');
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

export function inverse(a:number, n:number) :  number {
    let {gcd, x} = xgcd(a,  n);

    if (gcd !== 1){
        throw new Error('Inverse does not exist.');
    }
    
    return (x % n + n) % n;
}