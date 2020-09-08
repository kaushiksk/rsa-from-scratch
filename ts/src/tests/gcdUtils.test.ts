import { recursiveGCD, gcd, xgcd, ExtendedGCDReturnValue } from '../gcdUtils';

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
        expect(recursiveGCD(7, 0)).toBe(7);
        expect(recursiveGCD(0, 7)).toBe(7);
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
        expect(gcd(7, 0)).toBe(7);
        expect(gcd(0, 7)).toBe(7);
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
        let xgcdReturnValue: ExtendedGCDReturnValue = xgcd(7, 0);
        expect(xgcdReturnValue.gcd).toBe(7);
    });
});
