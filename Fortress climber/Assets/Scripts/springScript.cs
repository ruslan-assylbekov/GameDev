using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class springScript : MonoBehaviour
{
    private float time;

    void Start()
    {
        
    }

    void Update()
    {
        time += Time.deltaTime;
        if (time > 3)
        {
            Destroy(gameObject);
        }
    }
}
