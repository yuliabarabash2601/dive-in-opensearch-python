import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TypeaheadSearch.css';

const TypeaheadSearch = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
    const [isDropdownVisible, setIsDropdownVisible] = useState(true);
    const [baseURL, setBaseURL] = useState("http://0.0.0.0:8000/search_as_you_type/autocomplete");

    useEffect(() => {
      console.log("query", query);

      axios.get(`${baseURL}?query=${query}`)
        .then(response => {
            console.log("response", response);
          setResults(response.data);
        })
        .catch(error => {
          console.error("Error fetching typeahead results:", error);
        });
  }, [query]);

   const handleSelect = (value) => {
    // Update the query when an item is selected
    setQuery(value);
    // Hide the dropdown
  };
    const handleBaseURLChange = (e) => {
        console.log("baseURL", e.target.value);
        setQuery(""); // clear the query
        setResults([])
    setBaseURL(e.target.value);
  };

  return (
    <div className="typeahead-container">
        {/* Dropdown to select the base URL */}
      <select onChange={handleBaseURLChange} className="baseurl-selector">
        <option value="http://0.0.0.0:8000/prefix_match/autocomplete">Prefix matching</option>
          <option value="http://0.0.0.0:8000/n_gram/autocomplete">Edge n-gram matching</option>
        <option value="http://0.0.0.0:8000/completion/autocomplete">Completion suggester</option>
        <option value="http://0.0.0.0:8000/search_as_you_type/autocomplete">Search as you type</option>
      </select>
      <input
        type="text"
        className="typeahead-input"
        placeholder="Search..."
        value={query}
        onChange={e => setQuery(e.target.value)}
        onFocus={() => results.length > 0 && setIsDropdownVisible(true)}
        onBlur={() => setTimeout(() => setIsDropdownVisible(true), 200)}
      />
      {isDropdownVisible && (
        <ul className="typeahead-dropdown">
          {results.map((result, index) => (
            <li
              key={index}
              className="typeahead-item"
              onClick={() => handleSelect(result)}
            >
              {result}
            </li>
          ))}
        </ul>
      )}
    </div>
    );
}

export default TypeaheadSearch;
