(function(n) {
    n.extend(n.ui.tabs.prototype, {
        rotation: null,
        rotationDelay: null,
        continuing: null,
        rotate: function(n, i) {
            var r = this,
                f = this.options,
                u, e;
            return (n > 1 || r.rotationDelay === null) && n !== undefined && (r.rotationDelay = n), i !== undefined && (r.continuing = i), u = r._rotate || (r._rotate = function(t) {
                clearTimeout(r.rotation);
                r.rotation = setTimeout(function() {
                    var n = f.selected;
                    r.select(++n < r.anchors.length ? n : 0)
                }, n);
                t && t.stopPropagation()
            }), e = r._unrotate || (r._unrotate = i ? function() {
                t = f.selected;
                u()
            } : function(n) {
                n.clientX && r.rotate(null)
            }), n ? (this.element.bind("tabsshow", u), this.anchors.bind(f.event + ".tabs", e), u()) : (clearTimeout(r.rotation), this.element.unbind("tabsshow", u), this.anchors.unbind(f.event + ".tabs", e), delete this._rotate, delete this._unrotate), n === 1 && (n = r.rotationDelay), this
        },
        pause: function() {
            var n = this,
                t = this.options;
            n.rotate(0)
        },
        unpause: function() {
            var n = this,
                t = this.options;
            n.rotate(1, n.continuing)
        }
    })
})(jQuery);