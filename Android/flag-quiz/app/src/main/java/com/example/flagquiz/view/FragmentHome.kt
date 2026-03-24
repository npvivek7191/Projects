package com.example.flagquiz.view

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.example.flagquiz.R
import com.example.flagquiz.databinding.FragmentHomeBinding

class FragmentHome : Fragment() {

    lateinit var fragmentHomeBinding : FragmentHomeBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        fragmentHomeBinding = FragmentHomeBinding.inflate(inflater, container, false)
        return fragmentHomeBinding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        fragmentHomeBinding.buttonStart.setOnClickListener {
            val fragmentQuiz = FragmentQuiz()
            // TODO
        }
    }
}