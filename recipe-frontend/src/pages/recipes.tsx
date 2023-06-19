import Head from 'next/head'
import { useState, useEffect, SetStateAction } from 'react';

type recipeData = {
  id: number;
  name: string;
};

export default function Recipes() {
  const [recipe, setRecipe] = useState('');
  const [recipes, setRecipes] = useState<recipeData[]>([]);

  useEffect(() => {
    async function fetchNotes() {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/recipes/`);
      const json = await res.json();
      console.log(json)
      setRecipes(json);
    }
    fetchNotes();
  }, [])

  function handleChange(e: { target: { value: SetStateAction<string>; }; }) {
    setRecipe(e.target.value);
  }

  async function handleSubmit() {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/recipes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: recipe,
      })
    })
    const json = await res.json();
    setRecipes([...recipes, json])
  }

  return (
    <div>
      <Head>
        <title>Recipes</title>
      </Head>
      <div className="container mx-auto p-10 m-10">
        <div className="flex flex-col">
          <h1 className="font-bold mb-3">Recipes</h1>
          <textarea value={recipe} onChange={handleChange} className="border-2" ></textarea>
          <div className="mx-auto p-3 m-5">
            <button onClick={handleSubmit} className="bg-green-500 p-3 text-white">Submit</button>
          </div>
          <div>
            <ul>
              {recipes && recipes.map((recipe) =>
                  <li key={recipe.id} className="bg-yellow-100 m-3 p-3 border-yellow-200 border-2">{recipe.name}</li>
              )}
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}