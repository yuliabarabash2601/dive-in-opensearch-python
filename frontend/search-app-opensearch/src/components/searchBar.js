import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TypeaheadSearch.css';

const TypeaheadSearch = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
    const [isDropdownVisible, setIsDropdownVisible] = useState(false);

  useEffect(() => {
      console.log("query", query);
    if (query.length > 3) {
      axios.get(`http://0.0.0.0:8000/search_as_you_type/autocomplete?query=${query}`)
        .then(response => {
            console.log("response", response);
          setResults(response.data);
        })
        .catch(error => {
          console.error("Error fetching typeahead results:", error);
        });
    } else {
      setResults([]);
    }
  }, [query]);

   const handleSelect = (value) => {
    // Update the query when an item is selected
    setQuery(value);
    // Hide the dropdown
    setIsDropdownVisible(false);
  };

  return (
    <div className="typeahead-container">
      <input
        type="text"
        className="typeahead-input"
        placeholder="Search..."
        value={query}
        onChange={e => setQuery(e.target.value)}
        onFocus={() => results.length > 0 && setIsDropdownVisible(true)}
        onBlur={() => setTimeout(() => setIsDropdownVisible(false), 200)}
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
