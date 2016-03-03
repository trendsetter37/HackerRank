module.exports = {
    curry: function(fn, n) {
        if(typeof n !== 'number') {
            n = fn.length;
        }

        function getCurriedFn(prev) {
            return function(arg) {
                // concat teh just-specified arguments with the array of
                // previously-specified arguments.
                var args = prev.concat(arg);
                if(args.length < n) {
                    // not all arguments have been satisfied yet, so return a curried
                    // version of the original function.
                    return getCurriedFn(args);
                } else {
                    // Otherwise, invoke the original function with the args and
                    // return its value
                    return fn.apply(this, args);
                }
            };
        }
        // Return a curried version of the original function.
        return getCurriedFn([]);
    }

};
