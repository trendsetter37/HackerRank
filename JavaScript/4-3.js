var frankenCurry = function(fn, n) {
    if (typeof n !== 'number') {
        n = fn.length;
    }

    function getFrankenCurriedFn(prev) {
        return function() {
            var args = prev.concat(Array.prototype.slice.call(arguments, 0));
            if (args.length < n) {
              return getFrankenCurriedFn(args);
            } else {
              return fn.apply(this, args);
            }
        };
    }
    return getFrankenCurriedFn([]);
};

var add = (a, b) => a + b;

var bindFirstArg = function (fn, a) {
    // rel. flexible, more specific function generator
    return function(b) {
        return fn(a, b);
    }
};

var multiply = (a, b) => a * b;
var partialRight = function(fn) {
    var slice = Array.prototype.slice;
    var args = slice.call(arguments, 1);

    return function() {
        return fn.apply(this, slice.call(arguments, 0).concat(args));
    };
};
var partial = function(fn) {
    // ref. Arrray#slice method.
    var slice = Array.prototype.slice;
    // convert arguments object to an array, removing the first arg
    var args = slice.call(arguments, 1);

    return function() {
        // invoke the originally-specified function,
        // passing in all originally-specified arguments
        return fn.apply(this, args.concat(slice.call(arguments, 0)));
    };
};
var addAllTheThings = function() {
    var sum = 0;
    for( var i = 0; i < arguments.length; i++) {
      sum += arguments[i];
    }
    return sum;
};

var wedgie = function(a, b) {
    return a + ' gives ' + b + ' a wedgie.';
}

module.exports = {
    frankenCurry: frankenCurry,
    add: add,
    bindFirstArg: bindFirstArg,
    multiply: multiply,
    addAllTheThings: addAllTheThings,
    partial: partial,
    partialRight: partialRight,
    wedgie: wedgie
}
