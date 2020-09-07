import { recursiveGCD } from '../gcdUtils';

describe('recursiveGCD', () => {
  it("throw error if any argument is negative",  () =>  {
    expect(() => recursiveGCD(-1, 10)).toThrow(Error);
    expect(() => recursiveGCD(10, -1)).toThrow(Error);
    expect(() => recursiveGCD(-1, -1)).toThrow(Error);
  });

  it("should return 1 for co-primes",  () =>  {
    expect(recursiveGCD(7, 19)).toBe(1);
  });

  it("should return correct gcd when exists",  () =>  {
    expect(recursiveGCD(221,34)).toBe(17);
    expect(recursiveGCD(34,221)).toBe(17);
  });
});