
class CustomPaginate {

    constructor(data, per_page = 10, page_number = 1) {
        this.data = data;
        this.per_page = per_page;
        this.page_number = page_number;
    }

    /**Return the total number of pages*/
    get total_pages() {
        return Math.ceil(this.data.length / this.per_page);
    }

    get current_page() {
        return this.page_number;
    }

    /**Return if the current page has a next page*/
    get hasNextPage() {
        return this.page_number < this.total_pages;
    }

    getFirstPage() {
        return this.data.slice(0, this.per_page);
    }
}


export default CustomPaginate;