// Test-only browser init script: simulate a device without a WebGL context.
const originalContext = HTMLCanvasElement.prototype.getContext;
HTMLCanvasElement.prototype.getContext = function(type, ...args) {
  if (/webgl/i.test(type)) return null;
  return originalContext.call(this, type, ...args);
};
