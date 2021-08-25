//import Vue from "vue";

new Vue({
    el: '#app',
    data: {
        name: '',
        currency_from: [
            { name: "USD", desc: "US Dollar" },
            { name: "EUR", desc: "Euro" },
            { name: "GBP", desc: "British Pound" }
        ],
        convert_from: "USD",
        convert_to: "EUR",
        amount: ""
    },
    computed: {
        final_amount: function () {
            let to = this.convert_to;
            let from = this.convert_from;
            let final;
            switch (from) {
                case "GBP":
                    if (to == "USD") {
                        final = this.amount * 1.39;
                    }
                    if (to == "EUR") {
                        final = this.amount * 1.18;
                    }
                    if (to == "GBP") {
                        final = this.amount;
                    }
                    break;
                case "USD":
                    if (to == "USD") {
                        final = this.amount;
                    }
                    if (to == "EUR") {
                        final = this.amount * 0.85;
                    }
                    if (to == "GBP") {
                        final = this.amount * 0.72;
                    }
                    break;
                case "EUR":
                    if (to == "USD") {
                        final = this.amount * 1.17;
                    }
                    if (to == "EUR") {
                        final = this.amount;
                    }
                    if (to == "GBP") {
                        final = this.amount * 0.85;
                    }
                    break;
            }
            const formatter = new Intl.NumberFormat('en-US', {
                minimumFractionDigits: 2,      
                maximumFractionDigits: 2,
             });
             
            return formatter.format(final)
        }
    }
});