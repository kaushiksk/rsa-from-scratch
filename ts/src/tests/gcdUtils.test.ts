import { recursiveGCD, gcd, xgcd, inverse, ExtendedGCDReturnValue } from '../gcdUtils';

describe('recursiveGCD', () => {
    it('throw error if any argument is negative', () => {
        expect(() => recursiveGCD(-1, 10)).toThrow(Error);
        expect(() => recursiveGCD(10, -1)).toThrow(Error);
        expect(() => recursiveGCD(-1, -1)).toThrow(Error);
    });

    it('should return 1 for co-primes', () => {
        expect(recursiveGCD(7, 19)).toBe(1);
    });

    it('should return correct gcd when exists', () => {
        expect(recursiveGCD(221, 34)).toBe(17);
        expect(recursiveGCD(34, 221)).toBe(17);
    });

    it('should handle the case when input is zero', () => {
        expect(() => recursiveGCD(7, 0)).toThrow(Error);
        expect(() => recursiveGCD(0, 7)).toThrow(Error);
    });
});

describe('gcd', () => {
    it('throw error if any argument is negative', () => {
        expect(() => gcd(-1, 10)).toThrow(Error);
        expect(() => gcd(10, -1)).toThrow(Error);
        expect(() => gcd(-1, -1)).toThrow(Error);
    });

    it('should return 1 for co-primes', () => {
        expect(gcd(7, 19)).toBe(1);
    });

    it('should return correct gcd when exists', () => {
        expect(gcd(221, 34)).toBe(17);
        expect(gcd(34, 221)).toBe(17);
    });

    it('should handle the case when input is zero', () => {
        expect(() => gcd(7, 0)).toThrow(Error);
        expect(() => gcd(0, 7)).toThrow(Error);
    });
});

describe('xgcd', () => {
    it('throw error if any argument is negative', () => {
        expect(() => xgcd(-1, 10)).toThrow(Error);
        expect(() => xgcd(10, -1)).toThrow(Error);
        expect(() => xgcd(-1, -1)).toThrow(Error);
    });

    it('should return gcd 1 for co-primes', () => {
        let xgcdReturnValue: ExtendedGCDReturnValue = xgcd(7, 19);
        expect(xgcdReturnValue.gcd).toBe(1);
    });

    it('should return correct values when exist', () => {
        expect(xgcd(15, 35)).toStrictEqual({ gcd: 5, x: -2, y: 1 });
        expect(xgcd(30, 20)).toStrictEqual({ gcd: 10, x: 1, y: -1 });
    });

    it('should handle the case when input is zero', () => {
        expect(() => xgcd(7, 0)).toThrow(Error);
    });
});

describe('inverse', () => {
    const greaterThanZeroMockString: string = 'Both numbers have to be > 0';

    it('throw error if any argument is negative', () => {
        expect(() => inverse(-1, 10)).toThrow(greaterThanZeroMockString);
        expect(() => inverse(10, -1)).toThrow(greaterThanZeroMockString);
        expect(() => inverse(-1, -1)).toThrow(greaterThanZeroMockString);
    });

    it('should return correct inverse for co-primes', () => {
        expect(inverse(2, 5)).toBe(3);
        expect(inverse(17, 39)).toBe(23);
    });

    it('throw error when inverse gcd != 1', () => {
        expect(() => inverse(2, 4)).toThrow('Inverse does not exist.');
    });

    it('should handle the case when input is zero', () => {
        expect(() => inverse(7, 0)).toThrow(greaterThanZeroMockString);
    });
});
